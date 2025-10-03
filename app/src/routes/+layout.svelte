<script>
	import "../app.css";
	import favicon from "$lib/assets/eagle0.png";

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<main class="w-screen h-screen bg-zinc-950 text-zinc-200 p-2 font-serif">
	{@render children?.()}
</main>
