<script lang="ts">
    import { onMount } from "svelte";
    import { get } from "svelte/store";

    import { navigate } from "svelte-routing";

    import { get_token, remove_token, isAuthenticated } from "../stores/auth";


    const SERVER_IP = import.meta.env.VITE_API_SERVER_IP;

    async function logout() {
        const res = await fetch(`${SERVER_IP}/api/logout`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${get_token()}`
            },
        })
        if (res.ok) {
            remove_token();
            navigate('/login');
        } else {
            console.error('Logout failed');
        }
    }

    onMount(() => {
        // console.log(localStorage.getItem('token'))
        if (!get(isAuthenticated)) {
            navigate('/login');
        }
        logout();
    });

</script>