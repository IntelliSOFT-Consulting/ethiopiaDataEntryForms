$(function() {


    Object.keys(frenchTranslationData).forEach((indicatorClass) => {
        let data = frenchTranslationData[indicatorClass];




        // option
        $(`option[value=${indicatorClass}]`).text(data.shortHand);

        // No disaggregation
        $(`tr.${indicatorClass}.${indicatorClass}Enabled td`).first().html(data.indicator)

        // disaggregation

        let dataPoints = data.dataPoints;

        if (dataPoints.length) {
            let tds = $(`tr.${indicatorClass}.${indicatorClass}Disabled td`);

            let groupSize = tds.length / dataPoints.length;
            let position = 0;


            for (let i in tds) {

                if (i % groupSize == 0) {
                    tds[i].innerHTML = dataPoints[position];
                    position += 1;
                }
            }
        }

    })
})