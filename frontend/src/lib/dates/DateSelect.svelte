<script lang='ts'>
    import type { SvelteComponent } from 'svelte';
    import ErrorCard from "../ui/ErrorCard.svelte";

    export let header = "";
    export let width = "auto";
    export let isTimezone = false;
    export let dateOnly = false;
    export let padding = "3px 10px";

    let tzOffsets = Array.from({length: 24}, (_, i) => {
        let hroffset = i - 11;
        return hroffset < 0 ? hroffset : `+${hroffset}`
    });
    
    let inputElem: HTMLInputElement;
    let selectElem: HTMLSelectElement;
    let errorCard: SvelteComponent;

    export function setError(): void {
        errorCard.setError();
    }

    export function clearError(): void {
        errorCard.clearError();
    }

    export function getValue(): string {
        return isTimezone? selectElem.value: inputElem.value;
    }
</script>

<div style="width: {width}">
    {#if header}
        <h3>
            {header}
        </h3>
    {/if}
    <ErrorCard bind:this={errorCard}>
        {#if isTimezone}
            <select bind:this={selectElem}
                name="Timezone"
                class="inputBox tzbox"
                style="padding: {padding}"
            >
                {#each tzOffsets as tzoffset}
                    <option value={tzoffset}>{`UTC${tzoffset}`}</option>
                {/each}
            </select>
        {:else}
            {#if dateOnly}
                <input bind:this={inputElem} class="inputBox"
                    style="padding: {padding}"
                    type="date"
                    min="2022-01-01" max="2099-01-01">
            {:else}
                <input bind:this={inputElem} class="inputBox"
                    style="padding: {padding}"
                    type="datetime-local"
                    min="2022-01-01" max="2099-01-01">
            {/if}
        {/if}
    </ErrorCard>
</div>

<style>
    div {
        position: relative;
    }
    h3 {
        margin-top: 0;
        margin-bottom: 10px;
    }
    .inputBox {
        z-index: 5;
        color: inherit;
        cursor: pointer;
        border-radius: 10px;
        border: none;
        font-size: 12pt;
        background-color: #162a37;
        border: 2px solid transparent;
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(45deg, #1c9bab 0%, #0e6764) border-box;
        filter: drop-shadow(0px 10px 5px rgba(0, 0, 0, 0.3));
    }
    .inputBox:focus {
        outline: none;
        border: 2px solid #f04f1e;
    }

    .tzbox {
        background: linear-gradient(#12232E, #12232E) padding-box,
                    linear-gradient(270deg, #1c9bab 0%, #0e6764) border-box;
    }

    option {
        background-color: #12232E;
    }
</style>