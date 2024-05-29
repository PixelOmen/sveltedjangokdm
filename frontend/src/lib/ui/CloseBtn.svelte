<button on:click>
    &#10005;
    <!-- <img src={img_closeBtn} alt="" width={size} height={size}> -->
</button>

<style>
    button {
        padding: 5px 20px;
        /* padding-top: 8px; */
        cursor: pointer;
        outline: none;
        border: none;
        /* border: 1px solid rgb(0, 0, 0); */
        /* border-top: none; */
        background-color: rgba(0, 0, 0, 0);
        margin: 0;
        filter: saturate(0.9);
        text-align: center;
        color: inherit;
    }
    button:hover {
        filter: brightness(110%);
        background: linear-gradient(45deg, #a43d17, #b96017 99%);
        /* border: 1px solid rgba(0, 0, 0, 0); */
        /* border-top: none; */
        border-radius: 3px;
    }
    button:active {
        filter: brightness(80%);
    }
</style>