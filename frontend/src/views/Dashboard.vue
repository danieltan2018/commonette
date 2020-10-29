<template>
  <v-main>
    youtube: {{youtubeTop}}<br>
    book:{{ bookTop }}
    <div class="row">
      <div class="col-lg-4" >
        <v-card type="chart">
          <template slot="header">
            <!-- <h5 class="card-category">{{$t('dashboard.totalShipments')}}</h5> -->
            <h3 class="card-title"><i class="tim-icons icon-bell-55 text-primary "></i> 763,215</h3>
          </template>
          <div class="chart-area">
            <line-chart style="height: 100%" chart-id="purple-line-chart" :chart-data="purpleLineChart.chartData" :gradient-colors="purpleLineChart.gradientColors" :gradient-stops="purpleLineChart.gradientStops" :extra-options="purpleLineChart.extraOptions">
            </line-chart>
          </div>
        </v-card>
      </div>
      <div class="col-lg-4">
        <v-card type="chart">
          <template slot="header">
            <!-- <h5 class="card-category">{{$t('dashboard.dailySales')}}</h5> -->
            <h3 class="card-title"><i class="tim-icons icon-delivery-fast text-info "></i> 3,500€</h3>
          </template>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="blue-bar-chart" :chart-data="blueBarChart.chartData" :gradient-stops="blueBarChart.gradientStops" :extra-options="blueBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-lg-4">
        <v-card type="chart">
          <template slot="header">
            <!-- <h5 class="card-category">{{$t('dashboard.completedTasks')}}</h5> -->
            <h3 class="card-title"><i class="tim-icons icon-send text-success "></i> 12,100K</h3>
          </template>
          <div class="chart-area">
            <line-chart style="height: 100%" chart-id="green-line-chart" :chart-data="greenLineChart.chartData" :gradient-stops="greenLineChart.gradientStops" :extra-options="greenLineChart.extraOptions">
            </line-chart>
          </div>
        </v-card>
      </div>
    </div>
  </v-main>
</template>

<script>
import LineChart from '../components/Charts/LineChart';
import BarChart from '../components/Charts/BarChart';
import * as chartConfigs from '../components/Charts/config';
import config from '../config';
import axios from "axios";
export default {
  components: {
    LineChart,
    BarChart,
  },
  data: () => ({
    userCount: JSON.parse(localStorage.getItem("roomUsers")).length,
    youtubeTop: [],
    bookTop: [],
    movieTop: [],
    spotifyTop: [],
    purpleLineChart: {
      extraOptions: chartConfigs.purpleChartOptions,
      chartData: {
        labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
        datasets: [{
          label: "Data",
          fill: true,
          borderColor: config.colors.primary,
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: config.colors.primary,
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: config.colors.primary,
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: [80, 100, 70, 80, 120, 80],
        }]
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.2, 0],
    },
    greenLineChart: {
      extraOptions: chartConfigs.greenChartOptions,
      chartData: {
        labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV'],
        datasets: [{
          label: "My First dataset",
          fill: true,
          borderColor: config.colors.danger,
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          pointBackgroundColor: config.colors.danger,
          pointBorderColor: 'rgba(255,255,255,0)',
          pointHoverBackgroundColor: config.colors.danger,
          pointBorderWidth: 20,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 15,
          pointRadius: 4,
          data: [90, 27, 60, 12, 80],
        }]
      },
      gradientColors: ['rgba(66,134,121,0.15)', 'rgba(66,134,121,0.0)', 'rgba(66,134,121,0)'],
      gradientStops: [1, 0.4, 0],
    },
    blueBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: ['USA', 'GER', 'AUS', 'UK', 'RO', 'BR'],
        datasets: [{
          label: "Countries",
          fill: true,
          borderColor: config.colors.info,
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          data: [53, 20, 10, 80, 100, 45],
        }]
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    }
  }),
  created() {
    this.initialise();
  },
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    initialise() {
      axios
        .get("/recommend/" + localStorage.getItem("roomCode"))
        .then((response) => {
          this.youtubeTop = response.data.youtube.videoMore.split(",");
          this.bookTop = response.data.book.subject.split(",");
          this.movieTop = response.data.movie.genre.split(",");
          this.spotifyTop = response.data.spotify.seed_genres.split(",");
        })
        .catch(() => {
          this.navigateRoute("/questionnaire");
        });
    },
  },
  computed: {
    enableRTL() {
      return this.$route.query.enableRTL;
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
    bigLineChartCategories() {
      return this.$t('dashboard.chartCategories');
    }
  }
};
</script>
