<script context='module' lang='ts'>
    import type { AnchorData } from './NavAnchor.svelte';

    export type NavLinks = AnchorData[];    
</script>

<script lang='ts'>
    import logo from '/KDM_logo.png';
    import NavAnchor from './NavAnchor.svelte';
    
    export let navLinks: NavLinks;
</script>

<header class="container">
    <a href="/">
        <img src={logo} alt="Main Logo" width="40" height="40">
        <span>
            KDM-GEN
        </span>
    </a>
    <nav>
        <ul>
            {#each navLinks as link}
                <NavAnchor data={link}/>
            {/each}
        </ul>
    </nav>
</header>

<style>
    .container {
        font-family: 'montserrat', sans-serif;
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
        padding: 10px 0px;
    }
    a {
        text-decoration: none;
        display: flex;
        align-items: center;
    }
    a > span {
        outline: none;
        color: rgb(237, 237, 237);
        margin-left: 5px;
        font-size: 25pt;
        font-weight: 600;
    }
    ul {
        font-family: 'montserrat', sans-serif;
        padding-bottom: 4px;
        display: flex;
        gap: 20px;
    }

    @media (max-width: 1200px) {
        a > span {
            font-size: 20pt;
        }
        ul {
            gap: 5px;
        }
    }
</style>