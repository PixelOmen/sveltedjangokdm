<script lang='ts'>
    import { navigate } from "svelte-routing";

    import { save_token } from "../stores/auth";

    const SERVER_IP = import.meta.env.VITE_API_SERVER_IP;

    async function login() {
        const res = await fetch(`${SERVER_IP}/api/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "username": "eacosta",
                "password": "mypassword"
            })
        })
        if (res.ok) {
            const data = await res.json();
            save_token(data.token);
            navigate('/kdm');
        } else {
            console.log('Login failed');
        }
    }
</script>

<h3>
    This is the login page
    <div>
        <button on:click={login}>Login</button>
    </div>
</h3>