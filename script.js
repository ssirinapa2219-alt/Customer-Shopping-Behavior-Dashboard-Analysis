new Chart(
    document.getElementById("genderChart"),
    {
        type: "pie",
        data: {
            labels: ["Male","Female"],
            datasets: [{
                data: [5000,5000],
                backgroundColor: [
                    "#3498db",
                    "#e84393"
                ]
            }]
        },
        options:{
            plugins:{
                title:{
                    display:true,
                    text:"Gender Distribution"
                }
            }
        }
    }
);
 
new Chart(
    document.getElementById("categoryChart"),
    {
        type:"bar",
        data:{
            labels:[
                "Clothing",
                "Electronics",
                "Beauty",
                "Home",
                "Sports"
            ],
            datasets:[{
                label:"Customers",
                data:[
                    2200,
                    1800,
                    2000,
                    1700,
                    2300
                ],
                backgroundColor:"#2ecc71"
            }]
        },
        options:{
            plugins:{
                title:{
                    display:true,
                    text:"Category Distribution"
                }
            }
        }
    }
);
 
new Chart(
    document.getElementById("paymentChart"),
    {
        type:"doughnut",
        data:{
            labels:[
                "Credit Card",
                "Debit Card",
                "PayPal",
                "Cash"
            ],
            datasets:[{
                data:[
                    2600,
                    2400,
                    2500,
                    2500
                ],
                backgroundColor:[
                    "#9b59b6",
                    "#1abc9c",
                    "#f1c40f",
                    "#e67e22"
                ]
            }]
        },
        options:{
            plugins:{
                title:{
                    display:true,
                    text:"Payment Method Distribution"
                }
            }
        }
    }
);
 
new Chart(
    document.getElementById("ageChart"),
    {
        type:"line",
        data:{
            labels:[
                "18-25",
                "26-35",
                "36-45",
                "46-55",
                "56+"
            ],
            datasets:[{
                label:"Average Purchase (₹)",
                data:[
                    450,
                    620,
                    700,
                    580,
                    500
                ],
                borderColor:"#2980b9",
                backgroundColor:"#2980b9",
                fill:false,
                tension:0.4
            }]
        },
        options:{
            plugins:{
                title:{
                    display:true,
                    text:"Average Purchase by Age Group"
                }
            }
        }
    }
);
 