<script>
    import { onMount } from "svelte";
    import { writable } from "svelte/store";

    import data from "$lib/data/a.json";

    export let ele;
    const ix = writable(0);
    const accumulated = writable(false);
    let chart;

    const descriptions = [
        "Total unfiltered pages of federal regulation added per year. Since 1936",
        "Junk-filtered total pages of federal regulation added per year. Since 1975",
        "Category-based pages of federal regulation added per year. Since 1975",
    ];

    function set_chart(series) {
        chart = Highcharts.chart(ele, {
            // chart: {
            //     type: "bar",
            // },
            chart: { backgroundColor: "black" },
            title: {
                text: null,
            },
            xAxis: {
                categories: data["x_axis"],
            },
            yAxis: {
                title: {
                    text: "#",
                },
            },
            series:series 
        });
    }

    onMount(() => {
        ix.subscribe((y) => {
            let series_i = [];
            let acc_i = "not_accumulated";

            console.log(y);

            if (y == 0) {
                series_i = [{ name: "Total", data: data[acc_i]["total"] }];
            }
            if (y == 1) {
                series_i = [{ name: "Actual", data: data[acc_i]["actual"] }];
            }
            if (y == 2) {
                series_i = [
                    { name: "presidential", data: data[acc_i]["presidential"] },
                    { name: "rules", data: data[acc_i]["rules"] },
                    // { name: "actual", data: data[acc_i]["actual"] },
                ];
            }

            set_chart(series_i)
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
                <p class="col-span-6">
                    {descriptions[$ix]}
                </p>

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
