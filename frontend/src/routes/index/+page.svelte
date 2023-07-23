<script>
    export let data;
    // console.log(data);
    console.log(data);
</script>

<h1>총 ISBN 등록 개수 :</h1>

{#each data.cnt as item, idx}
    <div>{item.name} : {item.count.count} / {data.all_cnt.count}</div>
{/each}