<script context="module" lang="ts">
    import type { ListItemData } from '../../lib/search/ListItem.svelte'
    import type { SvelteComponent } from 'svelte';
</script>

<script lang='ts'>
    import ErrorCard from '../../lib/ui/ErrorCard.svelte';
    export let selected: ListItemData | null = null;

    let errorCard: SvelteComponent;

    let displayName: string;
    $: {
        if (selected === null) {
            displayName = "None";
        } else {
            displayName = selected.displayName;
        }
    }

    export function setError(): void {
        errorCard.setError();
    }

    export function clearError(): void {
        errorCard.clearError();
    }
</script>

<div>
    <h4>
        Selected:
    </h4>
    <ErrorCard bind:this={errorCard}>
        <div class="displayBox" title={displayName}>
            {displayName}
        </div>
    </ErrorCard>
</div>


<style>
    div {
        position: relative;
    }
    h4 {
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .displayBox {
        cursor: default;
        font-size: 11pt;
        font-weight: bold;
        border: 1px solid rgb(52, 51, 51);
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 5px;
        background-color: #1a333a;
        border: 2px solid transparent;
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(270deg, #1c9bab 10%, #0e6764) border-box;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
</style>