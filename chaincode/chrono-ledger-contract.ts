/*
 * SPDX-License-Identifier: Apache-2.0
 */

import { Context, Contract, Info, Returns, Transaction } from 'fabric-contract-api';
import { ChronoLedger } from './chrono-ledger';

@Info({title: 'ChronoLedgerContract', description: 'Luxury Watch Chaincode' })
export class ChronoLedgerContract extends Contract {

    @Transaction()
    public async InitChronoLedger(ctx: Context): Promise<void> {
        await this.RegisterMyWatch(ctx, 'W001', 'Rolex Boutique', 'ROLEX', 'Datejust 41', 'R111111', 'John', '01/05/2015', 'Owned')
        await this.RegisterMyWatch(ctx, 'W002', 'The Hour Glass', 'BREITING','NAVITIMER B01 CHRONOGRAPH 46', 'B111111', 'Richard', '01/06/2015', 'Owned')
        await this.RegisterMyWatch(ctx, 'W003', 'Gassan        ', 'ROLEX', 'Submariner Date 116613LB', 'R222222', 'Richard', '01/07/2015', 'Owned')
        await this.RegisterMyWatch(ctx, 'W005', 'The Hour Glass', 'BLANCPAIN', 'Le Brassus Chronograph Perpetual', 'L222222', 'John', '01/09/2015', 'Owned')
        await this.RegisterMyWatch(ctx, 'W006', 'Rolex Boutique', 'ROLEX', 'GMT-Master II Pepsi 116719BLRO', 'R333333', 'Mary', '01/10/2015', 'Owned')
        await this.RegisterMyWatch(ctx, 'W007', 'The Hour Glass', 'BREITING', 'Superocean Heritage B20', 'B333333', 'Mary', '01/11/2015', 'Owned') 
        await this.RegisterMyWatch(ctx, 'W008', 'Rolex Boutique', 'ROLEX', 'Zenith Movement 16589SACI', 'R444444', 'Richard', '01/12/2015', 'Owned')
    }

    @Transaction(false)
    @Returns('boolean')
    public async MyWatchExists(ctx: Context, chronoLedgerId: string): Promise<boolean> {
        const data: Uint8Array = await ctx.stub.getState(chronoLedgerId);
        return (!!data && data.length > 0);
    }


    @Transaction()
    public async RegisterMyWatch(ctx: Context, chronoLedgerId: string, AuthDealer: string, Brand: string, Model:string, SerialNo: string, Owner: string, OwnershipDate: string, Status: string ): Promise<void> {
        const exists: boolean = await this.MyWatchExists(ctx, chronoLedgerId);
        if (exists) {
            throw new Error(`The 'ChronoLedger ID ${chronoLedgerId} already exists`);
        }
        const chronoLedger: ChronoLedger = new ChronoLedger();
        chronoLedger.AuthDealer = AuthDealer;
        chronoLedger.Brand = Brand;
        chronoLedger.Model = Model;
        chronoLedger.SerialNo = SerialNo;
        chronoLedger.Owner = Owner;
        chronoLedger.OwnershipDate = OwnershipDate;
        chronoLedger.Status = Status;
        const buffer: Buffer = Buffer.from(JSON.stringify(chronoLedger));
        await ctx.stub.putState(chronoLedgerId, buffer);
    }


    @Transaction(false)
    @Returns('ChronoLedger')
    public async ReadMyWatch(ctx: Context, chronoLedgerId: string): Promise<ChronoLedger> {
        const exists: boolean = await this.MyWatchExists(ctx, chronoLedgerId);
        if (!exists) {
            throw new Error(`The ChronoLedger ID ${chronoLedgerId} does not exist`);
        }
        const data: Uint8Array = await ctx.stub.getState(chronoLedgerId);
        const chronoLedger: ChronoLedger = JSON.parse(data.toString()) as ChronoLedger;
        return chronoLedger;
    }

    @Transaction()
    public async UpdateMyWatchOwner(ctx: Context, chronoLedgerId: string, newOwner: string, newOwnershipDate: string): Promise<void> {
        const exists: boolean = await this.MyWatchExists(ctx, chronoLedgerId);
        if (!exists) {
            throw new Error(`The Chronoledger ID ${chronoLedgerId} does not exist`);
        }
        const data: Uint8Array = await ctx.stub.getState(chronoLedgerId);
        const chronoLedger: ChronoLedger = JSON.parse(data.toString()) as ChronoLedger;       
        // const chronoLedger: ChronoLedger = new ChronoLedger();

        chronoLedger.Owner = newOwner;
        chronoLedger.OwnershipDate = newOwnershipDate;
     
        const buffer: Buffer = Buffer.from(JSON.stringify(chronoLedger));
        await ctx.stub.putState(chronoLedgerId, buffer);
    }

    @Transaction()
    public async UpdateMyWatchStatus(ctx: Context, chronoLedgerId: string, newstatus: string): Promise<void> {
        const exists: boolean = await this.MyWatchExists(ctx, chronoLedgerId);
        if (!exists) {
            throw new Error(`The ChronoLedger ID ${chronoLedgerId} does not exist`);
        }
        const data: Uint8Array = await ctx.stub.getState(chronoLedgerId);
        const ChronoLedger: ChronoLedger = JSON.parse(data.toString()) as ChronoLedger;
        ChronoLedger.Status = newstatus;
        const buffer: Buffer = Buffer.from(JSON.stringify(ChronoLedger));
        await ctx.stub.putState(chronoLedgerId, buffer);
    }
 
    
    @Transaction()
    public async deleteMyWatch(ctx: Context, chronoLedgerId: string): Promise<void> {
        const exists: boolean = await this.MyWatchExists(ctx, chronoLedgerId);
        if (!exists) {
            throw new Error(`The Chronoledger ID ${chronoLedgerId} does not exist`);
        }
        await ctx.stub.deleteState(chronoLedgerId);
    }
    
    @Transaction(false)
    @Returns('ChronoLedger')
    public async ReadMyWatchHistory(ctx: Context, chronoLedgerId: string): Promise<string> {
        const exists: boolean = await this.MyWatchExists(ctx, chronoLedgerId);
        if (!exists) {
            throw new Error(`The ChronoLedger ID ${chronoLedgerId} does not exist`);
        }
        const history = await ctx.stub.getHistoryForKey(chronoLedgerId);
        const allResults = [];
        while (true) {
            const res = await history.next();
            if (res.value && res.value.value.toString()) {
                console.log(res.value.value.toString());
    
                const Key = chronoLedgerId;
                let Record;
                try {
                    Record = JSON.parse(res.value.value.toString());
                } catch (err) {
                    console.log(err);
                    Record = res.value.value.toString();
                }
                allResults.push({ Key, Record });
            }
            if (res.done) {
                console.log('end of data');
                await history.close();
                console.info(allResults);
                return JSON.stringify(allResults);
            }
        }
    }

    
    @Transaction(false)
    public async ReadAllWatchAssets(ctx: Context): Promise<string> {
        const startKey = 'W000';
        const endKey = 'W999';
        const iterator = await ctx.stub.getStateByRange(startKey, endKey);
        const allResults = [];
        while (true) {
            const res = await iterator.next();
            if (res.value && res.value.value.toString()) {
                console.log(res.value.value.toString());

                const Key = res.value.key;
                
                let Record;
                try {
                    Record = JSON.parse(res.value.value.toString());
                } catch (err) {
                    console.log(err);
                    Record = res.value.value.toString();
                }
                allResults.push({ Key, Record });
            }
            if (res.done) {
                console.log('end of data');
                await iterator.close();
                console.info(allResults);
                return JSON.stringify(allResults);
            }
        }
    }

    @Transaction(false)
    public async ReadAllWatchBrandAssets(ctx: Context, Brand: string): Promise<string> {
        const startKey = 'W000';
        const endKey = 'W999';
        const iterator = await ctx.stub.getStateByRange(startKey, endKey);
        const allResults = [];
        while (true) {
            const res = await iterator.next();
 
            if (res.value && res.value.value.toString()) {

                const data: Uint8Array = await ctx.stub.getState(res.value.key);
                const ChronoLedger: ChronoLedger = JSON.parse(data.toString()) as ChronoLedger;
                if (ChronoLedger.Brand == Brand) {
                    console.log(res.value.value.toString());
                    const Key = res.value.key;
                    let Record;
                    try {
                        Record = JSON.parse(res.value.value.toString());
                    } catch (err) {
                        console.log(err);
                        Record = res.value.value.toString();
                    }
                    allResults.push({ Key, Record });
                }
            }
            if (res.done) {
                console.log('end of data');
                await iterator.close();
                console.info(allResults);
                return JSON.stringify(allResults);
            }
        }
    }

    @Transaction(false)
    public async ReadStatus(ctx: Context, Status: string): Promise<string> {
        const startKey = 'W000';
        const endKey = 'W999';
        const iterator = await ctx.stub.getStateByRange(startKey, endKey);
        const allResults = [];
        while (true) {
            const res = await iterator.next();
 
            if (res.value && res.value.value.toString()) {

                const data: Uint8Array = await ctx.stub.getState(res.value.key);
                const ChronoLedger: ChronoLedger = JSON.parse(data.toString()) as ChronoLedger;
                if (ChronoLedger.Status == Status) {
                    console.log(res.value.value.toString());
                    const Key = res.value.key;
                    let Record;
                    try {
                        Record = JSON.parse(res.value.value.toString());
                    } catch (err) {
                        console.log(err);
                        Record = res.value.value.toString();
                    }
                    allResults.push({ Key, Record });
                }
            }
            if (res.done) {
                console.log('end of data');
                await iterator.close();
                console.info(allResults);
                return JSON.stringify(allResults);
            }
        }
    }

    @Transaction(false)
    public async ReadAllMyWatch(ctx: Context, Owner: string): Promise<string> {
        const startKey = 'W000';
        const endKey = 'W999';
        const iterator = await ctx.stub.getStateByRange(startKey, endKey);
        const allResults = [];
        while (true) {
            const res = await iterator.next();
 
            if (res.value && res.value.value.toString()) {

                const data: Uint8Array = await ctx.stub.getState(res.value.key);
                const ChronoLedger: ChronoLedger = JSON.parse(data.toString()) as ChronoLedger;
                if (ChronoLedger.Owner == Owner) {
                    console.log(res.value.value.toString());
                    const Key = res.value.key;
                    let Record;
                    try {
                        Record = JSON.parse(res.value.value.toString());
                    } catch (err) {
                        console.log(err);
                        Record = res.value.value.toString();
                    }
                    allResults.push({ Key, Record });
                }
            }
            if (res.done) {
                console.log('end of data');
                await iterator.close();
                console.info(allResults);
                return JSON.stringify(allResults);
            }
        }
    }
}
