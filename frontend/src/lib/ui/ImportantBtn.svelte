<script lang='ts'>
    export let content = "MyButton";
    export let fontSize = "13pt";
    export let fontWeight = "900";
    export let padding = "3px 15px";
    export let hasShadow = true;
    export let isClose = false;
    // export let hasBG = true;

    let shadowSpec = hasShadow? "filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.3))" : "";
    let paddingBottom = isClose? "padding-bottom: 6px;" : "";
</script>

<button 
    on:click 
    style="font-size: {fontSize};
    font-weight: {fontWeight};
    padding: {padding};
    {paddingBottom};
    {shadowSpec};
    "
>
    {content}
</button>

<style>
    button {
        background: linear-gradient(45deg, #a43d17, #b96017 99%);
        cursor: pointer;
        border: none;
        outline: none;
        border-radius: 5px;
        color: rgb(218, 218, 218);
        font-family: inherit;
    }
    button:hover {
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.3)) brightness(110%) !important;
    }
    button:active {
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.0)) !important;
    }
</style>