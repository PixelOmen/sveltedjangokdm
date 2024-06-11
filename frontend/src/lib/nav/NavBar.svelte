<script context='module' lang='ts'>
    import type { AnchorData } from './NavAnchor.svelte';

    export type NavLinks = AnchorData[];    
</script>

<script lang='ts'>
    import logo from '/film_can.svg';
    import NavAnchor from './NavAnchor.svelte';
    
    export let navLinks: NavLinks;
    let sidebar: HTMLElement;

    function toggleSidebar() {
        if (!sidebar.style.display) sidebar.style.display = 'none';
        sidebar.style.display = sidebar.style.display === 'none' ? 'flex' : 'none';
    }
</script>

<header class="container">
    <a href="/">
        <img src={logo} alt="Main Logo" width="40" height="40">
        <span>
            KDM&#x2011;GEN
        </span>
    </a>
    <nav>
        <ul class='navUL'>
            {#each navLinks as link}
                <NavAnchor data={link}/>
            {/each}
        </ul>
        <button class="hamburger" on:click={toggleSidebar}>
            &#9776;
        </button>
        <div bind:this={sidebar} class="sidebar">
            <button on:click={toggleSidebar} class="closeBtn">&#8617;</button>
            <ul class='sidebarUL'>
                {#each navLinks as link}
                    <NavAnchor data={link}/>
                {/each}
            </ul>
        </div>
    </nav>
</header>

<style>
    @media (max-width: 1000px) {
        .navUL {
            display: none !important;
        }
    }

    @media (min-width: 1001px) {
        .hamburger {
            display: none !important;
        }
    }

    @media (max-width: 700px) {
        a {
            font-size: 0.8em !important;
        }
    }

    .container {
        font-family: 'montserrat', sans-serif;
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 90%;
        margin-left: auto;
        margin-right: auto;
        padding: 10px 0px;
    }
    a {
        text-decoration: none;
        display: flex;
        align-items: center;
    }

    a > img {
        transform: translateY(-2px);
    }
    a > span {
        outline: none;
        color: rgb(237, 237, 237);
        margin-left: 5px;
        font-size: 2.5em;
        font-weight: 600;
    }
    .navUL {
        font-family: 'montserrat', sans-serif;
        padding-bottom: 4px;
        display: flex;
        gap: 30px;
    }

    .hamburger {
        font-size: 3em;
        margin-right: 10px;
        cursor: pointer;
        background: none;
        border: none;
    }

    .hamburger:active {
        outline: none;
        border: none;
    }

    .sidebar {
        display: none;
        flex-direction: column;
        position: fixed;
        top: 0;
        right: 0;
        background: radial-gradient(circle, rgba(19, 75, 130, 1) 0%, rgba(9, 50, 90, 0.95) 100%);
        width: max-content;
        height: 100%;
        z-index: 100;
        padding: 0px 50px;
    }

    .closeBtn {
        width: 100%;
        align-self: flex-end;
        font-size: 3em;
        margin-top: 30px;
        padding-bottom: 0px;
        background: none;
        border: none;
        /* border: 3px solid rgb(218, 128, 2); */
        border-radius: 20%;
        color: white;
        cursor: pointer;
    }

    .sidebarUL {
        display: flex;
        flex-direction: column;
        gap: 20px;
        margin-top: 40px;
    }

</style>