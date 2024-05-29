<script lang='ts'>
    export let errMsg = "-Required-";

    let errorCard: HTMLDivElement;
    let borderRadius = "10px 10px 0px 0px";
    let topOffset = "3px";

    $: {
        if (errorCard) {
            errorCard.style.setProperty('--borderRadius', borderRadius);
            errorCard.style.setProperty('--topOffset', topOffset);
        }
    }
        

    export function setError(): void {
        errorCard.classList.remove("hidden");
        errorCard.classList.remove("errorCardEnd");
        setTimeout(() => {
            errorCard.classList.add("errorCardEnd");
        }, 100);
    }

    export function clearError(): void {
        errorCard.classList.add("hidden");
    }
</script>


<div bind:this={errorCard} class="hidden errorCardStart errorCardEnd">
    {errMsg}
</div>
<slot></slot>


<style>
    div {
        --borderRadius: "";
        --topOffset: "";
    }
    .errorCardStart {
        border: 2px solid rgb(1, 131, 120);
        position: relative;
        top: 10px;
        left: 10%;
        width: 80%;
        text-align: center;
        color: rgb(255, 0, 0);
        font-family: inherit;
        font-weight: bold;
        background-color: #183549;
        border-radius: var(--borderRadius);
        transition: top 0.3s;
    }

    .errorCardEnd {
        top: var(--topOffset);
    }

    .hidden {
        display: none;
    }
</style>