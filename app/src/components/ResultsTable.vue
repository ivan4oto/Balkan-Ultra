<template>
  <div class="m-3">
    <b-container>
      <h3>Boys:</h3>
      <div class="results-frame-m">
        <b-table
          striped
          hover
          :items="mResults"
          :fields="fields"
          :tbody-tr-class="rowClass"
        ></b-table>
      </div>
      <h3 class="mt-2">Girls:</h3>
      <div class="results-frame-f">
        <b-table
          striped
          hover
          :items="fResults"
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
      mResults: [],
      fResults: [],
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
    var fResults = require("../assets/fresults.json");
    var mResults = require("../assets/mresults.json");
    this.fResults = fResults;
    this.mResults = mResults;
  },
};
</script>

<style scoped>
.results-frame-m {
  border: 10px solid lightseagreen;
}

.results-frame-f {
  border: 10px solid palevioletred;
}
</style>
