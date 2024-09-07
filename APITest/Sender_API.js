// install required package.
// $ npm install axios

const axios = require('axios');

async function sendEmail(reciever) {
    const API_URL = "https://emailsender000.pythonanywhere.com/send-email";

    const data = {
        email_reciever: reciever,
        msg_subject: 'Email Test',
        msg_body: 'This is the sample message using EmailSender API.',
        sender_name: 'EmailSender'
    };

    try {
        const response = await axios.post(API_URL, data, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log('success: ', response.data);
    }
    catch (error) {
        console.log('error: ', error.response ? error.response.data : error.message);  
    }
}

sendEmail('christiang03112003@gmail.com');
