<template>
  <div class="home">
    <b-container class='mt-4 d-none d-sm-block'>
      <ResultsTable />
    </b-container>
    <div class='d-block d-sm-none'>
      <ResultsTable />
    </div>
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
