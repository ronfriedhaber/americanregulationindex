<script>
    import { onMount } from "svelte";
    import { writable } from "svelte/store";

    export let ele;
    const ix = writable(0);
    const accumulated = writable(false);
    let chart;

    onMount(() => {
        chart = Highcharts.chart(ele, {
            // chart: {
            //     type: "bar",
            // },
            chart: { backgroundColor: "black" },
            title: {
                text: null,
            },
            xAxis: {
                categories: ["Apples", "Bananas", "Oranges"],
            },
            yAxis: {
                title: {
                    text: "Fruit eaten",
                },
            },
            series: [
                {
                    name: "Jane",
                    data: [1, 0, 4],
                },
                {
                    name: "John",
                    data: [5, 7, 3],
                },
            ],
        });
    });
</script>

<p class="fixed top-2 right-2 text-xs text-zinc-400">
    LAST UPDATED: OCTOBER 2025
</p>
<div class="h-full">
    <div class="flex flex-col place-items-center h-full p-2 gap-16 py-16 px-16">
        <div class="grid gap-8">
            <p class="text-2xl text-center">
                (UNOFFICAL) American Regulation Index
            </p>
            <p class="w-[80ch]">
                Is overregulation the root of stagnaion? What is regulation
                correlated with? By construcing a fairly polished, quantitive
                index derived from Federal data sources, The following
                micro-project aims at providing at least a partial answer to the
                aforementiond questions and more. While in some sense a dataset,
                and another a research report. Thanks to the federalreserve for
                constructing the building blocks upon which the Site is
                constucteed.
            </p>
        </div>

        <div class="grid grid-cols-3 gap-x-8 text-center">
            <span
                >Made By <a
                    class="underline"
                    href="https://x.com/ronfriedhaber"
                >
                    Ron Friedhaber</a
                ></span
            >

            <a
                class="underline"
                href="https://github.com/ronfriedhaber/americanregulationindex"
                >Code</a
            >
            <a class="underline" href="/datasources">Data Sources</a>
        </div>

        <div class="grid gap-4 border border-zinc-900 p-1 w-full">
            <div class="grid grid-cols-3">
                <button
                    on:click={() => {
                        ix.set(0);
                    }}
                    class="px-1 py-1 border border-zinc-400 border-zinc-900 hover:bg-zinc-800"
                    >TOTAL PAGES</button
                >
                <button
                    on:click={() => {
                        ix.set(1);
                    }}
                    class="px-1 py-1 border border-zinc-400 border-zinc-900 hover:bg-zinc-800"
                    >PAGES ACTUAL</button
                >
                <button
                    on:click={() => {
                        ix.set(2);
                    }}
                    class="px-1 py-1 border border-zinc-400 border-zinc-900 hover:bg-zinc-800"
                    >PAGES PER CATEGORY</button
                >
            </div>

            <div class="grid grid-cols-7 gap-x-4">
                <p class="col-span-4">
                    Index measuring total number of pages added to Federal Code
                    per year.
                </p>

                <p class="text-right text-zinc-400">SINCE: 1936-01-01</p>
                <p class="text-right text-zinc-400">UNTIL: 1936-01-01</p>

                <button
                    class="text-zinc-400 underline hover:text-zinc-300"
                    on:click={() => {
                        accumulated.set(!$accumulated);
                    }}
                >
                    {#if $accumulated}
                        YES ACCUMMULATED
                    {:else}
                        NOT ACCUMULATED
                    {/if}
                </button>
            </div>

            <div bind:this={ele}></div>
        </div>
    </div>
</div>
