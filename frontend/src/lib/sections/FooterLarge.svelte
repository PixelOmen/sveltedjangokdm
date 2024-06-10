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
    <div class="linksContainer">
        <nav>
            {#each navLinks as footerSection}
                <section>
                    <ul>
                        <NavAnchor data={footerSection}/>
                    </ul>
                </section>
            {/each}
        </nav>
    </div>
    <div class="legalContainer">
        This site utilizes DCP-o-matic © 2011-2024 Carl Hetherington and is distributed
        under the GNU General Public License (GPL) version 2 or later. 
        <br> For more information,
        visit <a href="https://dcpomatic.com">dcpomatic.com</a>.
    </div>
</footer>

<style>
    .footerContainer {
        max-width: 1300px;
        display: flex;
        padding-bottom: 20px;
        margin-left: auto;
        margin-right: auto;
        align-items: center;
        gap: 30px;
    }
    
    .linksContainer {
        flex: 1;
        width: max-content;
        white-space: nowrap;
        margin-right: 20px;
    }

    .legalContainer {
        flex: 4;
    }

    hr {
        margin-top: 0;
    }

    nav {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
    ul {
        font-size: 10pt;
    }
</style>