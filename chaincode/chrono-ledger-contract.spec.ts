/*
 * SPDX-License-Identifier: Apache-2.0
 */

import { Context } from 'fabric-contract-api';
import { ChaincodeStub, ClientIdentity } from 'fabric-shim';
import { ChronoLedgerContract } from '.';

import * as chai from 'chai';
import * as chaiAsPromised from 'chai-as-promised';
import * as sinon from 'sinon';
import * as sinonChai from 'sinon-chai';
import winston = require('winston');

chai.should();
chai.use(chaiAsPromised);
chai.use(sinonChai);

class TestContext implements Context {
    public stub: sinon.SinonStubbedInstance<ChaincodeStub> = sinon.createStubInstance(ChaincodeStub);
    public clientIdentity: sinon.SinonStubbedInstance<ClientIdentity> = sinon.createStubInstance(ClientIdentity);
    public logger = {
        getLogger: sinon.stub().returns(sinon.createStubInstance(winston.createLogger().constructor)),
        setLevel: sinon.stub(),
     };
}

describe('ChronoLedgerContract', () => {

    let contract: ChronoLedgerContract;
    let ctx: TestContext;

    beforeEach(() => {
        contract = new ChronoLedgerContract();
        ctx = new TestContext();
        ctx.stub.getState.withArgs('1001').resolves(Buffer.from('{"value":"chrono ledger 1001 value"}'));
        ctx.stub.getState.withArgs('1002').resolves(Buffer.from('{"value":"chrono ledger 1002 value"}'));
    });

    describe('#chronoLedgerExists', () => {

        it('should return true for a chrono ledger', async () => {
            await contract.chronoLedgerExists(ctx, '1001').should.eventually.be.true;
        });

        it('should return false for a chrono ledger that does not exist', async () => {
            await contract.chronoLedgerExists(ctx, '1003').should.eventually.be.false;
        });

    });

    describe('#createChronoLedger', () => {

        it('should create a chrono ledger', async () => {
            await contract.createChronoLedger(ctx, '1003', 'chrono ledger 1003 value');
            ctx.stub.putState.should.have.been.calledOnceWithExactly('1003', Buffer.from('{"value":"chrono ledger 1003 value"}'));
        });

        it('should throw an error for a chrono ledger that already exists', async () => {
            await contract.createChronoLedger(ctx, '1001', 'myvalue').should.be.rejectedWith(/The chrono ledger 1001 already exists/);
        });

    });

    describe('#readChronoLedger', () => {

        it('should return a chrono ledger', async () => {
            await contract.readChronoLedger(ctx, '1001').should.eventually.deep.equal({ value: 'chrono ledger 1001 value' });
        });

        it('should throw an error for a chrono ledger that does not exist', async () => {
            await contract.readChronoLedger(ctx, '1003').should.be.rejectedWith(/The chrono ledger 1003 does not exist/);
        });

    });

    describe('#updateChronoLedger', () => {

        it('should update a chrono ledger', async () => {
            await contract.updateChronoLedger(ctx, '1001', 'chrono ledger 1001 new value');
            ctx.stub.putState.should.have.been.calledOnceWithExactly('1001', Buffer.from('{"value":"chrono ledger 1001 new value"}'));
        });

        it('should throw an error for a chrono ledger that does not exist', async () => {
            await contract.updateChronoLedger(ctx, '1003', 'chrono ledger 1003 new value').should.be.rejectedWith(/The chrono ledger 1003 does not exist/);
        });

    });

    describe('#deleteChronoLedger', () => {

        it('should delete a chrono ledger', async () => {
            await contract.deleteChronoLedger(ctx, '1001');
            ctx.stub.deleteState.should.have.been.calledOnceWithExactly('1001');
        });

        it('should throw an error for a chrono ledger that does not exist', async () => {
            await contract.deleteChronoLedger(ctx, '1003').should.be.rejectedWith(/The chrono ledger 1003 does not exist/);
        });

    });

});
