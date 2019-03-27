module.exports = {
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        }
      ]
    }
  };

// module.exports = {
//     module: {
//         rules: [
//             {
//                 test: /.jsx?$/,
//                 loader: 'babel-loader',
//                 query: {
//                     presets: ['es2015', 'react']
//                 }
//             }
//         ]
//     }
// }