<script lang="ts">
    import { onMount } from "svelte";
    import { get } from "svelte/store";

    import { navigate } from "svelte-routing";

    import { get_token, remove_token, isAuthenticated } from "../stores/auth";

    const SERVER_IP = import.meta.env.VITE_API_SERVER_IP;

    async function logout() {
        await fetch(`${SERVER_IP}/api/logout`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${get_token()}`
            },
        })
        remove_token();
        navigate('/login');
    }

    onMount(() => {
        if (!get(isAuthenticated)) {
            navigate('/login');
        }
        logout();
    });

</script>

<svelte:head>
    <title>Logout</title>
</svelte:head>