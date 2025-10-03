<script>
    import { onMount } from "svelte";
    import { writable, get } from "svelte/store";
    import data from "$lib/data/a.json";

    export let ele; // chart target
    const ix = writable(0);
    const accumulated = writable(false);
    let chart;
    let chartEl; // bound container

    const descriptions = [
        "Total unfiltered pages of federal regulation added per year. Since 1936",
        "Junk-filtered total pages of federal regulation added per year. Since 1975",
        "Category-based pages of federal regulation added per year. Since 1975",
    ];

    function set_chart(series) {
        const opts = {
            chart: {
                backgroundColor: "black",
                reflow: true,              // let HC auto-fit to container
                spacing: [8, 8, 8, 8],
                style: { fontFamily: "ui-sans-serif, system-ui" }
            },
            title: { text: null },
            credits: { enabled: false },
            legend: { itemStyle: { color: "#e4e4e7" } },
            xAxis: {
                categories: data["x_axis"],
                labels: {
                    style: { color: "#a1a1aa" },
                    step:  Math.ceil(data["x_axis"].length / 8) // avoid crowding
                },
                lineColor: "#27272a",
                tickColor: "#27272a"
            },
            yAxis: {
                title: { text: null },
                labels: { style: { color: "#a1a1aa" } },
                gridLineColor: "#27272a"
            },
            tooltip: {
                backgroundColor: "#18181b",
                borderColor: "#3f3f46",
                style: { color: "#e4e4e7" }
            },
            series,
            responsive: {
                rules: [
                    {
                        condition: { maxWidth: 640 },
                        chartOptions: {
                            legend: { enabled: true },
                            xAxis: { labels: { step: Math.ceil(data["x_axis"].length / 4) } }
                        }
                    }
                ]
            }
        };

        chart = Highcharts.chart(ele, opts);
    }

    onMount(() => {
        // initial render
        const y = get(ix);
        updateSeries(y);

        // update on tab switch
        ix.subscribe(updateSeries);

        // reflow chart on container resize
        const ro = new ResizeObserver(() => {
            if (chart) chart.reflow();
        });
        if (chartEl) ro.observe(chartEl);

        // cleanup
        return () => ro.disconnect();
    });

    function updateSeries(y) {
        let series_i = [];
        let acc_i = get(accumulated) ? "accumulated" : "not_accumulated";

        if (y === 0) {
            series_i = [{ name: "Total", data: data[acc_i]["total"] }];
        } else if (y === 1) {
            series_i = [{ name: "Actual", data: data[acc_i]["actual"] }];
        } else {
            series_i = [
                { name: "presidential", data: data[acc_i]["presidential"] },
                { name: "rules", data: data[acc_i]["rules"] },
                { name: "proposed_rules", data: data[acc_i]["proposed_rules"] },
                { name: "notices", data: data[acc_i]["notices"] },
            ];
        }

        // create or update
        if (!chart) {
            set_chart(series_i);
        } else {
            while (chart.series.length) chart.series[0].remove(false);
            series_i.forEach(s => chart.addSeries(s, false));
            chart.redraw();
        }
    }
</script>

<!-- Fixed bits with safe-area padding and no overflow -->
<div class="fixed top-2 left-2 p-safe">
    <div class="grid grid-flow-col">
        <img src="/src/lib/assets/eagle0.png" alt="Eagle"
             class="w-7 h-7 sm:w-8 sm:h-8 object-contain" />
    </div>
</div>

<p class="fixed top-2 right-2 p-safe text-[10px] sm:text-xs text-zinc-400 truncate max-w-[50vw] sm:max-w-none">
    LAST UPDATED: OCTOBER 2025
</p>

<!-- Page container -->
<div class="min-h-screen w-full overflow-x-hidden">
    <div class="grid place-items-center min-h-screen gap-10 sm:gap-14 px-4 sm:px-6 lg:px-16 py-16">
        <!-- Title & intro -->
        <div class="grid gap-4 sm:gap-6 text-center">
            <p class="text-xl sm:text-2xl">
                (UNOFFICIAL) American Regulation Index
            </p>

            <p class="mx-auto max-w-prose text-sm sm:text-base text-zinc-200 leading-relaxed">
                Is overregulation the root of stagnation? What is regulation correlated with?
                By constructing a polished, quantitative index derived from federal data sources,
                this micro-project aims to provide at least a partial answer to those questions and more.
                Thanks to the Federal Reserve for constructing the building blocks upon which the site is built.
            </p>

            <p class="mx-auto max-w-prose text-xs sm:text-sm text-zinc-400 leading-relaxed">
                DISCLAIMER: While the site's codebase is completely open source and we strive for complete data correctness,
                data presented may be incorrect, flawed, skewed, or outright wrong.
            </p>
        </div>

        <!-- Links -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 sm:gap-x-8 text-center w-full max-w-3xl">
            <span>Made By
                <a class="underline break-all" href="https://x.com/ronfriedhaber">
                    Ron Friedhaber
                </a>
            </span>

            <a class="underline break-all" href="https://github.com/ronfriedhaber/americanregulationindex">
                Code
            </a>

            <a class="underline" href="/datasources">Data Source</a>
        </div>

        <!-- Card -->
        <div class="grid gap-4 border border-zinc-800/80 rounded-md p-2 sm:p-3 w-full max-w-7xl bg-black/20">
            <!-- Tabs -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                <button
                    on:click={() => ix.set(0)}
                    class="px-2 py-2 border border-zinc-900 hover:bg-zinc-800 rounded text-sm"
                >TOTAL PAGES</button>

                <button
                    on:click={() => ix.set(1)}
                    class="px-2 py-2 border border-zinc-900 hover:bg-zinc-800 rounded text-sm"
                >PAGES ACTUAL</button>

                <button
                    on:click={() => ix.set(2)}
                    class="px-2 py-2 border border-zinc-900 hover:bg-zinc-800 rounded text-sm"
                >PAGES PER CATEGORY</button>
            </div>

            <!-- Description + toggle -->
            <div class="grid grid-cols-1 sm:grid-cols-7 gap-3 sm:gap-x-4 items-start">
                <p class="sm:col-span-6 text-sm sm:text-base text-zinc-200">
                    {descriptions[$ix]}
                </p>

                <button
                    class="justify-self-start sm:justify-self-end text-xs sm:text-sm text-zinc-400 underline hover:text-zinc-300"
                    on:click={() => accumulated.set(!$accumulated)}
                >
                    {#if $accumulated}
                        YES ACCUMULATED
                    {:else}
                        NOT ACCUMULATED
                    {/if}
                </button>
            </div>

            <!-- Chart: fluid, non-overflowing -->
            <div class="w-full overflow-hidden">
                <div
                    bind:this={chartEl}
                    class="w-full max-w-full"
                >
                    <div bind:this={ele} class="w-full min-h-[320px] sm:min-h-[420px]"></div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    /* iOS safe-area utility (if Tailwind’s plugin not present) */
    .p-safe { padding-left: env(safe-area-inset-left); padding-right: env(safe-area-inset-right); }
</style>
