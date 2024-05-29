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