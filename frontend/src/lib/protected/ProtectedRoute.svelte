<script context='module' lang='ts'>
    import type { ComponentType } from 'svelte';
</script>

<script lang='ts'>
    import { onMount } from 'svelte';
    import { get } from 'svelte/store';

    import { navigate } from 'svelte-routing';

    import { isAuthenticated } from '../../stores/auth';

    export let component: ComponentType;

    let authenticated = false;

    onMount(() => {
        authenticated = get(isAuthenticated);
        if (!authenticated) {
            navigate('/login');
        }
    });
</script>

{#if authenticated}
    <svelte:component this={component} />
{:else}
    <p>Not authenticated</p>
{/if}