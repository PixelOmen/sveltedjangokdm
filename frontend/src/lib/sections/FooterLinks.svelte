<script lang='ts'>
    import NavAnchor from "../nav/NavAnchor.svelte";
    import type { AllNavSections } from "../nav/NavBar.svelte"

    export let paddingTop = "50px";
    export let showBorder = true;

    let allsections: AllNavSections = [];
    fetch("/api/nav")
        .then(res => res.json())
        .then(output => allsections = output);
</script>

<footer class="footerSection">
    <div class="footerContainer" style="padding-top: {paddingTop}">
        {#if showBorder}
            <hr />
        {/if}
        <nav>
            {#each allsections as footerSection}
                <section>
                    <h3>
                        {footerSection.sectionName}
                    </h3>
                    <ul>
                        {#each footerSection.contents as data}
                            <NavAnchor {data}/>
                        {/each}
                    </ul>
                </section>
            {/each}
        </nav>
    </div>
</footer>

<style>
    .footerSection {
        background: radial-gradient(
                ellipse at 20% -10%,
                #0e282f 0%,
                transparent 40%
        ), linear-gradient(#12232e 0%, #0a1c21 90%);
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
    h3 {
        font-weight: bold;
        margin: 10px 0px;
    }
    ul {
        font-size: 10pt;
    }    
</style>