import logo from './logo.svg';
import './App.css';

// import styled from "styled-components";

const Div = styled.div`
  display: flex;
  max-width: 494px;
`;

const Div2 = styled.div`
  display: flex;
  max-width: 382px;
`;

const Div3 = styled.div`
  display: flex;
  max-width: 382px;
  height: 398px;
  width: 382px;
  border-radius: 20px;
  background-color: rgba(255, 199, 115, 1);
`;

const Image1 = styled(Image)`
  display: flex;
  flex-grow: 1;
  position: relative;
  min-width: 20px;
  min-height: 20px;
  max-width: 382px;
`;

const Div4 = styled.div`
  display: flex;
  max-width: 206px;
`;

const Div5 = styled.div`
  display: flex;
  max-width: 206px;
  height: 206px;
  width: 206px;
  background-color: rgba(196, 196, 196, 1);
`;

const Image2 = styled(Image)`
  display: flex;
  position: relative;
  min-width: 20px;
  min-height: 20px;
  max-width: 205.31561279296875px;
  width: 205.31561279296875px;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  border-color: rgba(0, 0, 0, 1);
  border-width: 1px;
  border-style: solid;
`;

const Div6 = styled.div`
  display: flex;
  max-width: 0px;
`;

const Div7 = styled.div`
  display: flex;
  max-width: 363px;
`;

const Div8 = styled.div`
  max-width: 102px;
  color: rgba(255, 230, 193, 1);
  font-size: 17px;
  letter-spacing: 0%;
  text-align: left;
  font-family: PT Sans, sans-serif;
`;

const ImplementedAnOptimizedTsp = styled.div`
  max-width: 363px;
  color: rgba(255, 255, 255, 1);
  font-size: 14px;
  letter-spacing: 0%;
  text-align: left;
  font-family: PT Sans, sans-serif;
`;

const Div9 = styled.div`
  display: flex;
  max-width: 478px;
`;

const Div10 = styled.div`
  max-width: 115px;
  color: rgba(255, 230, 193, 1);
  font-size: 46px;
  letter-spacing: 0%;
  text-align: left;
  font-family: PT Sans, sans-serif;
`;

const Div11 = styled.div`
  max-width: 102px;
  color: rgba(255, 240, 217, 1);
  font-size: 16px;
  letter-spacing: 0%;
  text-align: left;
  font-family: PT Sans, sans-serif;
`;

const Div12 = styled.div`
  max-width: 357px;
  color: rgba(255, 255, 255, 1);
  font-size: 14px;
  letter-spacing: 0%;
  text-align: left;
  font-family: PT Sans, sans-serif;
`;

const Image4 = styled(Image)`
  display: flex;
  position: relative;
  min-width: 20px;
  min-height: 20px;
  max-width: 102px;
  width: 102px;
`;

export default function App(props) {
  return (
    <Div>
      <Div2>
        <Div3 />
        <Image1
          image="https://cdn.builder.io/api/v1/image/assets%2FTEMP%2F1340867c91c04a3db02c38036043cca5"
          backgroundPosition="center"
          backgroundSize="contain"
          aspectRatio={0.4083769633507853}
        />
      </Div2>
      <Div4>
        <Div5 />
        <Image2
          image="https://cdn.builder.io/api/v1/image/assets%2FTEMP%2Fef7c2839b5a74724a33ea5f5f25cf7bd"
          backgroundPosition="center"
          backgroundSize="contain"
          aspectRatio={1}
        />
      </Div4>
      <Image
        image="https://cdn.builder.io/api/v1/image/assets%2FTEMP%2F7d29f58eec51458a8fb221c0f73b6be3"
        backgroundPosition="center"
        backgroundSize="contain"
        aspectRatio={0.3246074496763539}
      />
      <Div6 />
      <Div7>
        <Div8>Contributions:</Div8>
        <ImplementedAnOptimizedTsp>
          Implemented an optimized “TSP” shortest-path algorithm Frontend and
          backend functionality Used: React.js, HTML, CSS, Django, Python3, and
          Figma
        </ImplementedAnOptimizedTsp>
      </Div7>
      <Div9>
        <Div10>Jibran</Div10>
        <Div11>Product Owner</Div11>
        <Div12>“Jayway”</Div12>
      </Div9>
      <Image4
        image="https://cdn.builder.io/api/v1/image/assets%2FTEMP%2F8d5124b657ca49c099e869e7fccef7ac"
        backgroundPosition="center"
        backgroundSize="cover"
        aspectRatio={0.6764705882352942}
      />
    </Div>
  );
}
