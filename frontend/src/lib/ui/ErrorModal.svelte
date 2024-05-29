<script lang='ts'>
    import CloseBtn from "./CloseBtn.svelte";
    import { addClickOutside, removeClickOutside } from "../../lib/clickEvents";

    let errMsg = "No error set";
    let container: HTMLDivElement;

    export function setError(err: string): void {
        errMsg = err;
    }

    export function show(): void {
        container.classList.remove("hidden");
        setTimeout(() => {
            addClickOutside(container, hide);
        }, 300);
    };

    export function hide(): void {
        container.classList.add("hidden");
        removeClickOutside(hide);
    };

</script>

<div bind:this={container} class="container hidden">
    <div class="header">
        <h4>
            Error Details:
        </h4>
        <div class="btn">
            <CloseBtn on:click/>
        </div>
    </div>
    <p>
        {errMsg}
    </p>
</div>

<style>
    .container {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border: 2px solid rgb(29, 29, 29);
        padding: 20px 20px;
        padding-top: 0px;
        padding-right: 10px;
        min-width: 500px;
        max-width: 80%;
        z-index: 100;
        background-color: #16323ae6;
        border-radius: 10px;
        filter: drop-shadow(5px 20px 10px rgba(0, 0, 0, 0.5));
    }
    @supports (backdrop-filter: blur(5px)) {
        .container {
            background-color: #16323ab0;
            backdrop-filter: blur(5px);
        }
    }

    .header {
        display: flex;
        margin-bottom: 15px;
        margin-right: 0px;
    }
    h4 {
        margin: 0;
        padding-top: 20px;
    }
    p {
        border: 1px solid black;
        margin: 0;
        margin-bottom: 10px;
        margin-right: 10px;
        padding: 0px 10px;
        background-color: #18262a;
        color: orange;
        white-space: pre-line;
        overflow-wrap: break-word;
    }
    .btn {
        margin-left: auto;
        padding-top: 5px;
        padding-right: 5px;
    }
    .hidden {
        display: none;
    }
</style>