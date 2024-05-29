<script context="module" lang="ts">
    import type { ListItemData } from './ListItem.svelte';
    type ListData = ListItemData[];
</script>

<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import SearchBox from './SearchBox.svelte';
    import ListItem from './ListItem.svelte';

    export let boxWidth = "auto";
    export let boxHeight = "auto";
    export let listData: ListData;
    export let header: string;
    export let searchPlaceholder = "Search";
    export let fileIcon = "";
    export let dirIcon = "";

    $: filteredData = listData;

    let searchInput: HTMLInputElement;
    $: {
        if (searchInput) {
            searchInput.addEventListener('change', () => {
                if (!searchInput.value) {
                    filteredData = listData;
                } else {
                    filteredData = listData.filter((item) => {
                        let lowerName = item.displayName.toLowerCase();
                        let lowerValue = searchInput.value.toLowerCase();
                        return lowerName.includes(lowerValue)
                    })
                }
            });
        }
    }

    export let selected: ListItemData|null = null;
    const dispatch = createEventDispatcher();
    function searchItemSelected(e: CustomEvent) {
        selected = e.detail;
        dispatch("searchItemSelected", {header: header, data: e.detail});
    }
</script>

<div class="container" style="width: {boxWidth}">
    <h3 style="margin-bottom: 10px">
        {header}
    </h3>
    <SearchBox bind:searchInput={searchInput} boxWidth="auto" placeholder="{searchPlaceholder}"/>
    <ul style="height: {boxHeight}">
        {#each filteredData as item}
            <ListItem 
                data={item}
                on:searchItemSelected={searchItemSelected}
                {fileIcon} {dirIcon}
            />
        {/each}
    </ul>
</div>

<style>
    .container {
        flex-direction: column;
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