<script lang='ts'>
    import LoadingIcon from "../../assets/LoadingIcon.png"
    export let width = "30px";
    export let height = "30px";
    export let offsetLeft = "35px";
    export let paddingTop = "0px";
</script>

<!-- <div style="width: {width}; height: {height}"></div> -->
<div>
    <img src={LoadingIcon} alt="Loading Icon" width={width} height={height}
        style="margin-left: {offsetLeft}; padding-top: {paddingTop}"
    >
</div>

<style>
    div {
        line-height: 0;
    }
    img {
        margin: 0;
        padding: 0;
        margin-right: auto;
        animation: spin 3s linear infinite;
    }

    @keyframes spin {
        0% { transform: rotate(0deg) }
        100% { transform: rotate(360deg) }
    }
</style>