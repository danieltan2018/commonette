import { Pie, mixins } from 'vue-chartjs'

export default {
    name: "pie-chart",
    extends: Pie,
    mixins: [mixins.reactiveProp],
    // props: ['options'],
    data () {
        return {
            ctx: null,
            options: {
                legend: {
                    display: true,
                    labels: {
                        fontColor: 'white'
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            }
        }
    },
    mounted () {
        this.renderChart(this.chartData, this.options)
    }
}