<script context="module" lang="ts">
    export interface ListItemData {
        displayName: string;
        isFile: boolean;
        isDir: boolean;
    }
</script>

<script lang='ts'>
    import { createEventDispatcher } from 'svelte';

    export let data: ListItemData;
    export let fileIcon = "";
    export let dirIcon = "";

    const dispatch = createEventDispatcher();
    function searchItemSelected() {
        dispatch("searchItemSelected", data);
    }

</script>


<li>
    <button class="container" on:click={searchItemSelected}>
        {#if data.isFile && fileIcon}
            <img src={fileIcon} alt="File Icon" width="20" height="20">
        {/if}
        {#if data.isDir && dirIcon}
            <img src={dirIcon} alt="File Icon" width="20" height="20">
        {/if}
        <div class="itemLabel" title={data.displayName}>
            {data.displayName}
        </div>
    </button>
</li>


<style>
    .container {
        background-color: #162a37;
        border: 1px solid black;
        border-radius: 5px;
        display: flex;
        width: 100%;
        padding: 8px 10px;
        font-family: inherit;
        color: inherit;
    }
    .container:hover {
        cursor: pointer;
        border-radius: 5px;
        background-color: #1a7c89;
        font-weight: 900;        
    }
    .itemLabel {
        padding: 0px 3px;
        font-size: 10pt;
        font-family: inherit;
        color: inherit;
        width: 100%;
        text-align: left;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 100%;
        background: rgba(0, 0, 0, 0);
        border: none;
    }
</style>