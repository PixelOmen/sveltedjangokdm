<script context="module" lang="ts">
    export interface ListItemData {
        id: number;
        display_name: string;
        isFile: boolean;
        isDir: boolean;
    }
</script>

<script lang='ts'>
    import { createEventDispatcher } from 'svelte';
    import trashcan from '../../assets/trashcan.svg';

    export let data: ListItemData;
    export let fileIcon = "";
    export let dirIcon = "";

    const dispatch = createEventDispatcher();
    function searchItemSelected() {
        dispatch("searchItemSelected", data);
    }

    function searchItemDeleted() {
        dispatch("searchItemDeleted", data);
    }

</script>


<li class="itemContainer">
    <button class="clickContainer" on:click={searchItemSelected}>
        {#if data.isFile && fileIcon}
            <img src={fileIcon} alt="File Icon" width="20" height="20">
        {/if}
        {#if data.isDir && dirIcon}
            <img src={dirIcon} alt="File Icon" width="20" height="20">
        {/if}
        <div class="itemLabel" title={data.display_name}>
            {data.display_name}
        </div>
    </button>
    <button class="trashBtn" title="Delete" on:click={searchItemDeleted}>
        <img class="trashSVG" src={trashcan} alt="Delete Icon" width="20">
    </button>
</li>


<style>
    .itemContainer {
        display: flex;
        width: 100%;
        box-sizing: border-box;
        flex-wrap: nowrap;
        overflow: hidden;
    }

    .clickContainer {
        background-color: #162a37;
        border: 1px solid black;
        border-radius: 5px;
        display: flex;
        padding: 8px 10px;
        font-family: inherit;
        color: inherit;
        overflow: hidden;
        width: 100%;
    }
    .clickContainer:hover {
        cursor: pointer;
        border-radius: 5px;
        background-color: #1a7c89;
        /* font-weight: 900; */
    }
    .itemLabel {
        max-width: 100%;
        padding: 1px 5px;
        font-size: 10pt;
        font-family: inherit;
        color: whitesmoke;
        text-align: left;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .trashBtn {
        background: none;
        border: none;
    }
        
    .trashSVG {
        cursor: pointer;
        margin-left: 0px;
        transition: margin 0.3s;
    }

    .trashSVG:hover {
        margin-left: 30px;
        filter: saturate(0%) brightness(300%) contrast(150%);
    }
</style>