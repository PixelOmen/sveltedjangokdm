<script lang='ts'>
    export let header = "";
    export let bgimg = "";
</script>

<section class="sectionContainer">
    <div class="imgContainer" style="background-image: url({bgimg});">
    </div>
        <div class="textContainer">
            <h4 class="header">
                {header}
            </h4>
            <p>
                <slot/>
            </p>
        </div>
</section>


<style>
    .sectionContainer {
        position: relative;
        display: flex;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
        justify-content: center;
        overflow: hidden;
        border-top: 2px solid #a46d39;
        border-bottom: 2px solid #a46d39;
    }

    .imgContainer {
        z-index: 0;
        position: absolute;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        width: 100%;
        height: 100%;
        filter: blur(10px) brightness(65%);
    }    
    .header {
        font-size: 20pt;
        margin: 0;
        font-weight: bold;
    }
    .textContainer {
        padding: 60px 0px;
        font-family: "Montserrat";
        z-index: 1;
        max-width: 650px;
        font-weight: bold;
        font-size: 11pt;
        text-align: center;
        color:rgb(230, 230, 230);
    }
</style>