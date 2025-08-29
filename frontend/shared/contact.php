<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit(0);
}

$messages_file = '/var/www/production-workspace/contact_messages.json';
$admin_email = 'otmane@zineinsight.com';

function sendSimpleEmail($name, $email, $message, $project) {
    global $admin_email;

    $subject = "Nouveau message de contact - $project";

    $body = "=== NOUVEAU MESSAGE DE CONTACT ===\n\n";
    $body .= "Nom: $name\n";
    $body .= "Email: $email\n";
    $body .= "Projet: $project\n\n";
    $body .= "Message:\n$message\n\n";
    $body .= "---\n";
    $body .= "Reçu le: " . date('d/m/Y à H:i:s') . "\n";
    $body .= "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . "\n";
    $body .= "Site: https://zineinsight.com\n";

    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();

    return @mail($admin_email, $subject, $body, $headers);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Recevoir un message de contact
    $input = json_decode(file_get_contents('php://input'), true);

    if (!$input) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Invalid JSON']);
        exit;
    }

    $name = trim($input['name'] ?? '');
    $email = trim($input['email'] ?? '');
    $message_text = trim($input['message'] ?? '');
    $project = trim($input['project'] ?? 'analytics');

    // Validation basique
    if (empty($name) || empty($email) || empty($message_text)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Nom, email et message sont requis']);
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Email invalide']);
        exit;
    }

    $message = [
        'id' => 'contact_' . time(),
        'name' => $name,
        'email' => $email,
        'message' => $message_text,
        'project' => $project,
        'timestamp' => date('c'),
        'ip' => $_SERVER['REMOTE_ADDR'] ?? 'unknown',
        'status' => 'new'
    ];

    // Charger messages existants
    $messages = [];
    if (file_exists($messages_file)) {
        $messages = json_decode(file_get_contents($messages_file), true) ?: [];
    }

    // Envoyer l'email (sans bloquer si ça échoue)
    $email_sent = sendSimpleEmail($name, $email, $message_text, $project);
    $message['email_sent'] = $email_sent;

    // Ajouter nouveau message
    $messages[] = $message;

    // Sauvegarder
    @file_put_contents($messages_file, json_encode($messages, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));

    // Réponse rapide
    echo json_encode([
        'success' => true,
        'message' => $email_sent ?
            'Message envoyé avec succès ! Nous vous répondrons rapidement.' :
            'Message reçu ! Nous vous répondrons rapidement.',
        'id' => $message['id']
    ]);

} elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Lister les messages (pour admin seulement)
    $messages = [];
    if (file_exists($messages_file)) {
        $messages = json_decode(file_get_contents($messages_file), true) ?: [];
    }

    echo json_encode([
        'success' => true,
        'messages' => $messages,
        'total' => count($messages)
    ]);

} else {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed']);
}
?>
