<script lang="ts">
    import SearchIcon from '../../assets/search_icon.svg';

    export let boxWidth = "200px";
    export let placeholder = "Test Placeholder";

    export let searchInput: HTMLInputElement;
</script>

<div class="container" style="width: {boxWidth}">
    <img src="{SearchIcon}" alt="Search Icon" width="20px">
    <input bind:this={searchInput} type="text" placeholder="{placeholder}">
</div>

<style>
    .container {
        border: 2px solid rgb(128, 128, 128);
        border-radius: 8px;
        display: flex;
        padding: 3px 10px;
        box-sizing: border-box;
    }
    input {
        color: inherit;
        margin-left: 5px;
        border: none;
        outline: none;
        background: none;
        width: 100%;
    }
    input::placeholder {
        color: grey;
    }
</style>