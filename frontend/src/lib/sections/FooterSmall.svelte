<script lang='ts'>
    import NavAnchor from "../nav/NavAnchor.svelte";
    import type { NavLinks } from "../nav/NavBar.svelte"

    export let navLinks: NavLinks;
    export let paddingTop = "50px";
    export let showBorder = false;
    export let width = "";
    
    const containerWidth = width ? width : "80%";
</script>

<footer class="footerContainer" style="padding-top: {paddingTop}; width: {containerWidth}">
        {#if showBorder}
            <hr />
        {/if}
        <nav>
            {#each navLinks as footerSection}
                <section>
                    <ul>
                        <NavAnchor data={footerSection}/>
                    </ul>
                </section>
            {/each}
        </nav>
</footer>

<style>
    @media (max-width: 1000px) {
        .footerContainer {
            min-width: 80% !important;
            max-width: 80% !important;
        }
    }

    .footerContainer {
        align-self: flex-start;
        width: 80%;
        padding-bottom: 20px;
        margin-left: auto;
        margin-right: auto;
        box-sizing: border-box;
    }

    hr {
        margin-top: 0;
    }

    nav {
        display: flex;
        justify-content: space-around;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
    ul {
        font-size: 10pt;
    }
</style>