<template>
  <div class="m-3">
      <div style="display: flex;
                 justify-content: center;
                 align-items: center"
            class="mb-2">
        <b-img src="../assets/icons/boy.png" fluid alt="Fluid image"></b-img>
        <h3></h3>
      </div>
      <div >
        <b-table
          small
          outlined
          striped
          responsive
          table-variant: dark
          text: info
          hover
          :items="mResults"
          :fields="fields"
          :tbody-tr-class="rowClass"
        ></b-table>
      </div>
      <div style="display: flex;
                 justify-content: center;
                 align-items: center"
            class="m-2">
        <b-img src="../assets/icons/girl.png" fluid alt="Fluid image"></b-img>
      </div>
      <div class="results-frame-f">
        <b-table
          small
          outlined
          striped
          responsive
          hover
          table-variant: dark
          :items="fResults"
          :fields="fields"
          :tbody-tr-class="rowClass"
        ></b-table>
      </div>
  </div>
</template>
<script>
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
      if (item.Ranking === "DNF") return "table-danger";
    },
  },
  mounted: function() {
    console.log("mounted");
    var fResults = require("../assets/fresults.json");
    var mResults = require("../assets/mresults.json");
    this.fResults = fResults;
    console.log(fResults);
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
