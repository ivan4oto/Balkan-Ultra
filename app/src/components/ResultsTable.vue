<template>
  <div class='m-3'>
    <b-container>
      <h3>Boys:</h3>
      <div class="results-frame">
        <b-table
          striped
          hover
          :items="boys"
          :fields="fields"
          :tbody-tr-class="rowClass"
        ></b-table>
        <h3>Girls:</h3>
        <b-table
          striped
          hover
          :items="girls"
          :fields="fields"
          :tbody-tr-class="rowClass"
        ></b-table>
      </div>
    </b-container>
  </div>
</template>
<script>
// const axios = require("axios").default;

export default {
  name: "ResultsTable",
  data() {
    return {
      fields: [
        {
          key: "Ranking",
          sortable: true,
        },
        {
          key: "First name",
          sortable: true,
        },
        {
          key: "Family name",
          sortable: false,
        },
        {
          key: "Time",
          // Variant applies to the whole column, including the header and footer
          variant: "",
        },
      ],
      boys: [],
    };
  },
  methods: {
    rowClass(item, type) {
      if (!item || type !== "row") return;
      if (item.Ranking !== "DNF") return "table-success";
      if (item.Ranking === "DNF") return "table-danger";
    },
  },
  mounted: function() {
    console.log("mounted");
    var results2020 = require("../assets/results2020.json");
    console.log(results2020);
    this.boys = results2020;
    console.log(this.boys);
  },
};
</script>

<style scoped>
.results-frame {
  border: 10px solid lightseagreen;
}
</style>
