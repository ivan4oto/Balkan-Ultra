<template>
  <div class="m-3">
      <div style="display: flex;
                 justify-content: center;
                 align-items: center"
            class="mt-2">
        <b-img src="../assets/pictures/men.jpg" fluid alt="Fluid image"></b-img>
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
            class="mt-4">
        <b-img src="../assets/pictures/women.jpg" fluid alt="Fluid image"></b-img>
      </div>
      <div>
        <b-table
          small
          outlined
          striped
          responsive
          hover
          table-variant: dark
          :items="fResults"
          :fields="fields"
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
  
  },
  mounted: function() {
    var fResults = require("../assets/fresults.json");
    var mResults = require("../assets/mresults.json");
    this.fResults = fResults;
    this.mResults = mResults;
  },
};
</script>

<style scoped>
</style>
