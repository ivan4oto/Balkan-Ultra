<template>
  <div class="home">
    <ResultsTable />
  </div>
</template>

<script>
// @ is an alias to /src
import ResultsTable from "@/components/ResultsTable.vue";

export default {
  name: "Results",
  components: {
    ResultsTable,
  },
};
</script>
