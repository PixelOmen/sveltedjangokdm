<script lang='ts'>
    export let content = "MyButton";
    export let fontSize = "13pt";
    export let fontWeight = "700";
    export let padding = "3px 15px";
    export let hasShadow = false;

    let shadowSpec = hasShadow? "filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.3))" : "";
</script>

<button 
    on:click 
    style="font-size: {fontSize};
    font-weight: {fontWeight};
    padding: {padding};
    {shadowSpec};
    "
>
    {content}
</button>

<style>
    button {
        /* background: linear-gradient(45deg, #a43d17, #b96017 99%); */
        background-color: #007BFF;
        cursor: pointer;
        border: none;
        outline: none;
        border-radius: 5px;
        color: rgb(218, 218, 218);
        font-family: inherit;
    }
    button:hover {
        filter: brightness(110%) !important;
    }
    button:active {
        filter: drop-shadow(1px 5px 5px rgba(0, 0, 0, 0.0)) !important;
    }
</style>