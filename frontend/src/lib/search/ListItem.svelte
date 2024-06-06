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


<li>
    <div class="itemContainer">
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
    </div>
</li>


<style>
    .itemContainer {
        display: flex;
        width: 100%;
    }
    .clickContainer {
        width: 100%;
        background-color: #162a37;
        border: 1px solid black;
        border-radius: 5px;
        display: flex;
        padding: 8px 10px;
        font-family: inherit;
        color: inherit;
    }
    .clickContainer:hover {
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

    .trashBtn {
        background: none;
        border: none;
        outline: none;
        }
        
    .trashSVG {
        cursor: pointer;
        padding-left: 0px;
        transition: padding 0.3s;
    }
    .trashSVG:hover {
        padding-left: 15px;
        filter: saturate(0%) brightness(300%) contrast(150%);
    }
</style>