<script context='module' lang='ts'>
    import type { SectionLinks } from './NavSection.svelte';
    export type AllNavSections = {
        sectionName: string;
        contents: SectionLinks;
    }[];    
</script>

<script lang='ts'>
    import { onMount, onDestroy } from 'svelte';
    import logo from '../../assets/logo.ico';
    import NavSection from './NavSection.svelte';
    
    let allsections: AllNavSections = [];

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
        fetch("/api/nav")
        .then(res => res.json())
        .then(output => allsections = output);
        window.addEventListener('click', clickOutside)
    })
    onDestroy(() => {
        window.removeEventListener('click', clickOutside)
    })
</script>

<header class="container">
    <a href="/">
        <img src={logo} alt="Main Logo" width="50" height="50">
        <span>
            ROUNDABOUT
        </span>
    </a>
    <nav bind:this={navElement}>
        <ul>
            {#each allsections as navsection}
                <NavSection
                    displayText={navsection.sectionName}
                    sectionData={navsection.contents}
                    sectionVisible={openSection === navsection.sectionName}
                    on:navSectionOpen={setOpenSection}
                />
            {/each}
        </ul>
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
        font-weight: 900;
        letter-spacing: -2px;
        font-stretch: ultra-condensed;
    }
    ul {
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