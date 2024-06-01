<script context='module' lang='ts'>
    import type { SectionLinks } from './NavSection.svelte';
    export type AllNavSections = {
        sectionName: string;
        contents: SectionLinks;
    }[];    
</script>

<script lang='ts'>
    import { onMount, onDestroy } from 'svelte';
    import logo from '../../assets/KDM_logo.png';
    import NavSection from './NavSection.svelte';
    
    export let navSections: AllNavSections;

    let openSection: string|null = null;
    function setOpenSection(e: CustomEvent): void {
        openSection = openSection === e.detail ? null : e.detail;
    }

    let navElement: HTMLElement;
    function clickOutside(e: Event): void {
        if (navElement && !navElement.contains(e.target as Node)) {
            openSection = null;
        }
    }

    onMount(() => {
        window.addEventListener('click', clickOutside)
    })
    onDestroy(() => {
        window.removeEventListener('click', clickOutside)
    })
</script>

<header class="container">
    <a href="/">
        <img src={logo} alt="Main Logo" width="40" height="40">
        <span>
            KDM-GEN
        </span>
    </a>
    <nav bind:this={navElement}>
        {#each navSections as section}
            <ul>
                <NavSection
                    displayText={section.sectionName}
                    sectionData={section.contents}
                    sectionVisible={openSection === section.sectionName}
                    on:navSectionOpen={setOpenSection}
                />
            </ul>
        {/each}
    </nav>
</header>

<style>
    .container {
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
        padding-bottom: 4px;
        display: flex;
        gap: 10px;
    }
    @media (max-width: 1200px) {
        .container {
            max-width: 90%;
        }
        a > span {
            font-size: 20pt;
        }
        ul {
            gap: 5px;
        }
    }
</style>