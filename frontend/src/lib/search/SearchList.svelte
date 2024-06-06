<script context="module" lang="ts">
    import type { ListItemData } from './ListItem.svelte';
    type ListData = ListItemData[];
</script>

<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import SearchBox from './SearchBox.svelte';
    import ListItem from './ListItem.svelte';
    import ImportantBtn from '../ui/ImportantBtn.svelte';

    export let listData: ListData;
    export let header: string;

    export let boxWidth = "auto";
    export let boxHeight = "auto";
    export let searchPlaceholder = "Search";
    export let fileIcon = "";
    export let dirIcon = "";
    export let filetypes = "";

    $: filteredData = listData.reverse();

    let searchInput: HTMLInputElement;
    $: {
        if (searchInput) {
            searchInput.addEventListener('change', () => {
                if (!searchInput.value) {
                    filteredData = listData;
                } else {
                    filteredData = listData.filter((item) => {
                        let lowerName = item.display_name.toLowerCase();
                        let lowerValue = searchInput.value.toLowerCase();
                        return lowerName.includes(lowerValue)
                    })
                }
            });
        }
    }

    let fileSelectInputActual: HTMLInputElement;
    function openFileSelect() {
        fileSelectInputActual.click();
    }
    $: {
        if (fileSelectInputActual) {
            fileSelectInputActual.addEventListener('change', () => {
                if (fileSelectInputActual.files?.length === 0 || fileSelectInputActual.files === null) return;
                let file = fileSelectInputActual.files[0];
                dispatch("fileAdded", {header: header, file: file});
            });
        }
    }


    export let selected: ListItemData|null = null;
    const dispatch = createEventDispatcher();
    function searchItemSelected(e: CustomEvent) {
        selected = e.detail;
        dispatch("searchItemSelected", {header: header, data: e.detail});
    }

    function searchItemDeleted(e: CustomEvent) {
        selected = e.detail;
        dispatch("searchItemDeleted", {header: header, data: e.detail});
    }

</script>

<div class="container" style="width: {boxWidth}">
    <h3 style="margin-bottom: 10px">
        {header}
    </h3>
    <div class="searchAddContainer">
        <SearchBox bind:searchInput={searchInput} boxWidth="100%" placeholder="{searchPlaceholder}"/>
        <div style="margin-left: 10px;">
            <ImportantBtn
                on:click={openFileSelect}
                content="+"
                fontSize="16pt"
                padding="1px 10px"
                hasShadow={false}
            />
        </div>
    </div>
    <ul style="height: {boxHeight}">
        {#if filteredData.length === 0}
            <li style="text-align: center; margin-top: 10px">
                Press 
                <ImportantBtn
                    on:click={openFileSelect}
                    content="+"
                    fontSize="10pt"
                    padding="5px 10px"
                    hasShadow={false}
                />
                to add a new item
            </li>
        {:else}
            {#each filteredData as item}
            <ListItem 
                data={item}
                on:searchItemSelected={searchItemSelected}
                on:searchItemDeleted={searchItemDeleted}
                {fileIcon} {dirIcon}
            />
            {/each}
        {/if}
    </ul>
    <input bind:this={fileSelectInputActual} type="file" class="fileSelect-btn-actual hidden" accept={filetypes} multiple={false}>
</div>

<style>
    .hidden {
        display: none;
    }

    .container {
        flex-direction: column;
    }

    .searchAddContainer {
        display: flex;
    }

    h3 {
        margin: 0;
    }

    ul {
        margin-top: 5px;
        border: 3px solid transparent;
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(90deg, #923214, #bd7532 90%) border-box;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        padding: 5px 5px;
        overflow: auto;
    }
</style>