<script lang='ts'>
    import TableCol from "./TableCol.svelte";

    export let tableData: Record<string, any>[];
    export let headers: {
        key: string,
        displayName: string,
        minwidth: string,
        payloadKey?: string
    }[];

    interface ColData {
        header: string,
        data: {displayName: string, payload: string}[],
        minwidth: string
    }

    let colData: ColData[] = [];

    $: {
        if (tableData && headers) {
            let reversed = tableData.reverse();
            let newData: ColData[] = [];
            headers.forEach(header => {
                let columnData = reversed.map(row => {
                    if (header.payloadKey) {
                        return {displayName: row[header.key], payload: row[header.payloadKey]}
                    } else {
                        return {displayName: row[header.key], payload: ""}
                    }
                });
                newData.push({
                    header: header.displayName,
                    data: columnData,
                    minwidth: header.minwidth
                });
            });
            colData = newData;
        }
    }
</script>

<table class="container">
    {#each colData as col}
        <TableCol
            on:tableCellClick
            header={col.header}
            data={col.data}
            minwidth={col.minwidth}/>
    {/each}
</table>


<style>
    .container {
        padding: 10px;
        width: 100%;
        display: flex;
        justify-content: center;
    }
</style>