import React from 'react';
import ReactDOM from 'react-dom';
import img1 from './img/img1.png';


ReactDOM.render(
    <h1>
        hello worldd!
        <img src={img1} />
    </h1>,
    document.getElementById('root')
);

if (module.hot) {
    module.hot.accept();
}

//const a = () => {console.log('arrow func')};