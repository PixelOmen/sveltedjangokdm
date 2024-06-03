<script lang='ts'>
    import NavAnchor from "../nav/NavAnchor.svelte";
    import type { NavLinks } from "../nav/NavBar.svelte"

    export let navLinks: NavLinks;
    export let paddingTop = "50px";
    export let showBorder = false;

    const ulDirection = navLinks.length > 1 ? "ulColumn" : "ulRow";
    const sectionWidth = navLinks.length > 1 ? "" : "fullSection";
</script>

<footer class="footerSection">
    <div class="footerContainer" style="padding-top: {paddingTop}">
        {#if showBorder}
            <hr />
        {/if}
        <nav>
            {#each navLinks as footerSection}
                <section class={sectionWidth}>
                    <ul class={ulDirection}>
                        <NavAnchor data={footerSection}/>
                    </ul>
                </section>
            {/each}
        </nav>
    </div>
</footer>

<style>
    .footerSection {
        flex: 1;
        display: flex;
        min-width: 900px;
    }

    hr {
        margin-top: 0;
    }

    .footerContainer {
        align-self: flex-start;
        width: 80%;
        padding-bottom: 20px;
        margin-left: auto;
        margin-right: auto;
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

    .fullSection {
        width: 100%;
    }

    .ulRow {
        width: 100%;
        display: flex;
        justify-content: space-around;

    }
</style>