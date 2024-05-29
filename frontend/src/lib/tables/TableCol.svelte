<script lang='ts'>
    import { createEventDispatcher } from "svelte";

    export let header: string;
    export let data: {displayName: string, payload: string}[];
    export let minwidth = "10px";

    const dispatch = createEventDispatcher();

    function handleDispatch(payload: string) {
        dispatch('tableCellClick', payload);
    }
</script>

<div class="container" style="min-width: {minwidth}">
    <h3>
        {header}
    </h3>
    <ul>
        {#each data as item}
            {#if item.payload}
                <li title={item.displayName}>
                    <button on:click={() => handleDispatch(item.payload)}>
                        {item.displayName}
                    </button>
                </li>
            {:else}
                <li title={item.displayName}>
                    {item.displayName}
                </li>
            {/if}
        {/each}
    </ul>
</div>

<style>
    .container {
        flex-grow: 1;
        overflow: hidden;
        font-size: 10pt;
        box-sizing: content-box;
        border: 1px solid #197a87;
        border-radius: 2px;
        background-color: #12232E;
    }
    h3 {
        padding: 0;
        margin: 5px 5px;
    }
    li {
        padding: 2px 10px;
        border-top: 1px solid #197a87;
        overflow: hidden;
        text-overflow: ellipsis;
        border-radius: 2px;
        white-space: nowrap;
    }
    button {
        padding: 0;
        font-family: inherit;
        font-size: inherit;
        margin: none;
        background: none;
        border: none;
        outline: none;
        cursor: pointer;
        text-decoration: underline;
        color: #ff7931;
    }
</style>