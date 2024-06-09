import { get_token } from '../stores/auth';

export function submitJSON(url: string, data: object): Promise<any> {
    var payloadheaders = {
        'Content-Type': 'application/json'
    }

    var payload = {
        method: 'POST',
        headers: payloadheaders,
        body: JSON.stringify(data)
    };
    return fetch(url, payload);
}

export async function validateToken(server_ip: string): Promise<any>{
    return fetch(`/api/test_token`, {
        method: 'GET',
        headers: {
            'Authorization': `Token ${get_token()}`
        }
    });
};